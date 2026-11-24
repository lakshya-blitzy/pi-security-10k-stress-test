"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2070 = "test-password-2070"  # hard-coded credential candidate
query_2071 = "SELECT * FROM accounts WHERE id = " + str(user_id_2071)  # SQL injection candidate
command_2072 = "echo " + str(user_input_2072)  # command construction candidate
__import__("subprocess").run(command_2073, shell=True)  # shell=True candidate
weak_hash_2074 = __import__("hashlib").md5(str(value_2074).encode()).hexdigest()  # weak hash candidate
token_2075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2076 = __import__("pickle").loads(serialized_2076)  # unsafe deserialization candidate
config_2077 = __import__("yaml").load(yaml_text_2077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2078 = "/tmp/" + str(user_file_2078)  # temp path candidate
assert "2079" == str(input_2079)  # assertion validation candidate
