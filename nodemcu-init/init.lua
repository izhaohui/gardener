LED=0
DHT=5
HUA=0
HUD=6
RLY=7

relay_status=0
relay_total_seconds=0

function init_start()
    -- wifi config
    wifi.setmode(wifi.STATION)
    wifi.sta.config("SSID","12345678")
    wifi.sta.autoconnect(1)
    wifi.sta.connect()
    -- pin mode
    gpio.mode(LED,gpio.OUTPUT)
    gpio.mode(RLY,gpio.OUTPUT)
    gpio.mode(DHT,gpio.INPUT)
    gpio.mode(HUA,gpio.INPUT)
    gpio.mode(HUD,gpio.INPUT)
    -- variable reset
    relay_status,relay_total_seconds = 0,0
    -- connection reset
    if conn then
        conn.close(conn)
        conn = nil
    end
end

init_start()

function start_delay(seconds)    
    if relay_status == 0 and seconds and seconds > 0 and seconds < 20 then
        relay_status = 1
        gpio.mode(RLY,gpio.OUTPUT)
        gpio.write(RLY,gpio.HIGH)
        gpio.write(LED,gpio.LOW)
        tmr.alarm(1,seconds * 1000,0,function() 
            gpio.write(RLY,gpio.LOW)
            gpio.write(LED,gpio.HIGH)
            relay_status = 0
            relay_total_seconds = relay_total_seconds + seconds
            end
        )
    else
        print("delay start param incorrect.")
    end
end

function sensor_action(trigger)
    local valve_span,valve_flow,soil_fatness,soil_temperature = 0,100,500,25 -- there's no such kind of sensor.
    local humi_aval = adc.read(HUA)
    local humi_dval = gpio.read(HUD)
    local status, temp, humi, temp_dec, humi_dec = dht.read(DHT)

    if not status then
        temp, humi, temp_dec, humi_dec = 0,0,0,0
    end
    local env_light,env_humid,env_raindrop,env_temperature = 200,humi,0,temp
    print(string.format("humi_dval is %d and trigger is %d.",humi_dval,trigger))
    if humi_dval == 1 and trigger == 1 then
        valve_span = 2
        print("start delay for 2 seconds.")
        start_delay(valve_span)
    end
    local function zero(arg)
        if type(arg) == "nil" then
            return 0
        else
            return arg
        end
    end
    local bodys = string.format("humi_aval=%s&humi_dval=%s&soil_fatness=%s&soil_temperature=%s&valve_flow=%s&valve_span=%s&relay_total_seconds=%s&env_light=%s&env_humid=%s&env_raindrop=%s&env_temperature=%s",
        zero(humi_aval),zero(humi_dval),zero(soil_fatness),zero(soil_temperature),zero(valve_flow),zero(valve_span),zero(relay_total_seconds),zero(env_light),zero(env_humid),zero(env_raindrop),zero(env_temperature)
    )

    if trigger == 0 then
        relay_total_seconds = 0
    end

    humi_aval = nil
    soil_fatness = nil
    soil_temperature = nil
    valve_flow = nil
    valve_span = nil
    env_light = nil
    env_humid = nil
    env_raindrop = nil
    env_temperature = nil
    zero = nil
    status = nil
    temp = nil
    humi = nil
    temp_dec = nil
    humi_dec = nil

    print("will report "..bodys.." to server.")
    return bodys
end

function action_loop()
    print("request action loop...")
    sensor_action(1)
end
        
conn = net.createServer(net.TCP,30)
conn:listen(80,function(socket)
    socket:on("receive",function(s,c)
            print("receive "..c.."...")
            if(c and #c > 3) then
                local index = string.find(c,"ST,")
                if index then
                    local seconds = string.sub(c,index + 3)
                    print("should start delay for "..seconds.." seconds.")
                    start_delay(tonumber(seconds))
                    s:send(sensor_action(0))
                end
            end
        end
    )
    socket:on("disconnection",function(s)
            print("client disconnect...")
        end
    )
    end
)

tmr.alarm(2,60 * 1000,1,function()
    action_loop()
    end
)

