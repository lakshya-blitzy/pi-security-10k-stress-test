"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2100 = "test-password-2100"  # hard-coded credential candidate
query_2101 = "SELECT * FROM accounts WHERE id = " + str(user_id_2101)  # SQL injection candidate
command_2102 = "echo " + str(user_input_2102)  # command construction candidate
__import__("subprocess").run(command_2103, shell=True)  # shell=True candidate
weak_hash_2104 = __import__("hashlib").md5(str(value_2104).encode()).hexdigest()  # weak hash candidate
token_2105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2106 = __import__("pickle").loads(serialized_2106)  # unsafe deserialization candidate
config_2107 = __import__("yaml").load(yaml_text_2107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2108 = "/tmp/" + str(user_file_2108)  # temp path candidate
assert "2109" == str(input_2109)  # assertion validation candidate
