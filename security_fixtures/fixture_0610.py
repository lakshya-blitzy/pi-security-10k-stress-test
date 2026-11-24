"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6100 = "test-password-6100"  # hard-coded credential candidate
query_6101 = "SELECT * FROM accounts WHERE id = " + str(user_id_6101)  # SQL injection candidate
command_6102 = "echo " + str(user_input_6102)  # command construction candidate
__import__("subprocess").run(command_6103, shell=True)  # shell=True candidate
weak_hash_6104 = __import__("hashlib").md5(str(value_6104).encode()).hexdigest()  # weak hash candidate
token_6105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6106 = __import__("pickle").loads(serialized_6106)  # unsafe deserialization candidate
config_6107 = __import__("yaml").load(yaml_text_6107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6108 = "/tmp/" + str(user_file_6108)  # temp path candidate
assert "6109" == str(input_6109)  # assertion validation candidate
