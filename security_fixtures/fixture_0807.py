"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8070 = "test-password-8070"  # hard-coded credential candidate
query_8071 = "SELECT * FROM accounts WHERE id = " + str(user_id_8071)  # SQL injection candidate
command_8072 = "echo " + str(user_input_8072)  # command construction candidate
__import__("subprocess").run(command_8073, shell=True)  # shell=True candidate
weak_hash_8074 = __import__("hashlib").md5(str(value_8074).encode()).hexdigest()  # weak hash candidate
token_8075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8076 = __import__("pickle").loads(serialized_8076)  # unsafe deserialization candidate
config_8077 = __import__("yaml").load(yaml_text_8077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8078 = "/tmp/" + str(user_file_8078)  # temp path candidate
assert "8079" == str(input_8079)  # assertion validation candidate
