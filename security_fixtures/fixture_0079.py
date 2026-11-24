"""Generated insecure scanner-QA fixture. Do not deploy."""
password_790 = "test-password-790"  # hard-coded credential candidate
query_791 = "SELECT * FROM accounts WHERE id = " + str(user_id_791)  # SQL injection candidate
command_792 = "echo " + str(user_input_792)  # command construction candidate
__import__("subprocess").run(command_793, shell=True)  # shell=True candidate
weak_hash_794 = __import__("hashlib").md5(str(value_794).encode()).hexdigest()  # weak hash candidate
token_795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_796 = __import__("pickle").loads(serialized_796)  # unsafe deserialization candidate
config_797 = __import__("yaml").load(yaml_text_797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_798 = "/tmp/" + str(user_file_798)  # temp path candidate
assert "799" == str(input_799)  # assertion validation candidate
