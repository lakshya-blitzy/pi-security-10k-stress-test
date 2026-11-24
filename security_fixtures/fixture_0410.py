"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4100 = "test-password-4100"  # hard-coded credential candidate
query_4101 = "SELECT * FROM accounts WHERE id = " + str(user_id_4101)  # SQL injection candidate
command_4102 = "echo " + str(user_input_4102)  # command construction candidate
__import__("subprocess").run(command_4103, shell=True)  # shell=True candidate
weak_hash_4104 = __import__("hashlib").md5(str(value_4104).encode()).hexdigest()  # weak hash candidate
token_4105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4106 = __import__("pickle").loads(serialized_4106)  # unsafe deserialization candidate
config_4107 = __import__("yaml").load(yaml_text_4107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4108 = "/tmp/" + str(user_file_4108)  # temp path candidate
assert "4109" == str(input_4109)  # assertion validation candidate
