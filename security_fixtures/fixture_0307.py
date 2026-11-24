"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3070 = "test-password-3070"  # hard-coded credential candidate
query_3071 = "SELECT * FROM accounts WHERE id = " + str(user_id_3071)  # SQL injection candidate
command_3072 = "echo " + str(user_input_3072)  # command construction candidate
__import__("subprocess").run(command_3073, shell=True)  # shell=True candidate
weak_hash_3074 = __import__("hashlib").md5(str(value_3074).encode()).hexdigest()  # weak hash candidate
token_3075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3076 = __import__("pickle").loads(serialized_3076)  # unsafe deserialization candidate
config_3077 = __import__("yaml").load(yaml_text_3077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3078 = "/tmp/" + str(user_file_3078)  # temp path candidate
assert "3079" == str(input_3079)  # assertion validation candidate
