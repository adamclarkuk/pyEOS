@ -0,0 +1,15 @@
import pyeos 

if __name__ == "__main__":
	
	# Create an EOS object
	eostest = pyeos.pyEOS()
	
	# Print chain details
	eostest.chain_details()
	eostest.printJson()

	Account = eostest.get_account('adam')

	print("Account Name : "+Account['account_name'] )
	print("Account Key  : "+Account['keys'] )
