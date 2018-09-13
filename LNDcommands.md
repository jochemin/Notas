#### Number of active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true) ] | length'
```
#### Number of inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false) ] | length'
```
#### Close all inactive channels
```
lncli listchannels | jq '.[][]' | jq -c -r 'select(.active == false) | .channel_point' | tr : ' ' | xargs -n2 lncli closechannel --force
```
#### List local balance in active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true and .local_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total local balance in active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true)] | map(.local_balance|tonumber) | add'
```
#### List remote balance in active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true and .remote_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total remote balance in active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true)] | map(.remote_balance|tonumber) | add'
```
#### List local balance in inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false and .local_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total local balance in inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false)] | map(.local_balance|tonumber) | add'
```
#### List remote balance in inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false and .remote_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total remote balance in inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false)] | map(.remote_balance|tonumber) | add'
```
#### Change channel fee to minimum
```
lncli updatechanpolicy --base_fee_msat 0 --fee_rate 0
```