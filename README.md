# nomitm
Development for no man in the middle

I am working on code to solve the problem of man in the middle. 
My development is to change the mac address periodically in a way would be difficult for the human to catch up your mac address. 
And using the https to cipher the data.
In this way would support the client side 
For Ubuntu fresh installed without internet connection
1. Use ufw default deny incoming
2. Use ufw deny http
3. Use screen or nohup for session
   Example 
            screen -S das 
            python3 GenerateMac.py
            ctrl+ A+ D for deattach to continue your work  
4. Copy the following code and name it as you want 
5. Periodically clear browser cache

you can change the thread timing if there were too many attacks to make the timing shorter

For windows i will work on the development which i will use the powershell to set the ip  link for documentation from microsoft
https://docs.microsoft.com/en-us/powershell/module/netadapter/set-netadapter?view=win10-ps

For android and iphone if anyone interessted can add a touch

I hope to continue developing it and to help many people as i could ;)
