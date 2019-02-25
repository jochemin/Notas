#### View Satoshis genesis quote (only non pruned nodes, launch from terminal in blocks folder)
```
hexdump -C -s 8 -n 285 blk00000.dat
```

#### bitcoin.conf 
-walletnotify=<cmd>
       Execute command when a wallet transaction changes (%s in cmd is replaced
       by TxID)
