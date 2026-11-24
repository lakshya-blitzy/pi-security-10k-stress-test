"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6070 = "test-password-6070"  # hard-coded credential candidate
query_6071 = "SELECT * FROM accounts WHERE id = " + str(user_id_6071)  # SQL injection candidate
command_6072 = "echo " + str(user_input_6072)  # command construction candidate
__import__("subprocess").run(command_6073, shell=True)  # shell=True candidate
weak_hash_6074 = __import__("hashlib").md5(str(value_6074).encode()).hexdigest()  # weak hash candidate
token_6075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6076 = __import__("pickle").loads(serialized_6076)  # unsafe deserialization candidate
config_6077 = __import__("yaml").load(yaml_text_6077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6078 = "/tmp/" + str(user_file_6078)  # temp path candidate
assert "6079" == str(input_6079)  # assertion validation candidate
