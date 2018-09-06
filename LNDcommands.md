#### Number of active channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true) ] | length'
```
#### Number of inactive channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==false) ] | length'
```
#### List local balance in channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true and .local_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total local balance
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true)] | map(.local_balance|tonumber) | add'
```
#### List remote balance in channels
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true and .remote_balance!="0") ] | .[] | .local_balance | tonumber'
```
#### Total remote balance
```
lncli listchannels | jq '[ .channels | .[] | select(.active==true)] | map(.remote_balance|tonumber) | add'
```
