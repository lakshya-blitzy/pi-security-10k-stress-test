"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7070 = "test-password-7070"  # hard-coded credential candidate
query_7071 = "SELECT * FROM accounts WHERE id = " + str(user_id_7071)  # SQL injection candidate
command_7072 = "echo " + str(user_input_7072)  # command construction candidate
__import__("subprocess").run(command_7073, shell=True)  # shell=True candidate
weak_hash_7074 = __import__("hashlib").md5(str(value_7074).encode()).hexdigest()  # weak hash candidate
token_7075 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7076 = __import__("pickle").loads(serialized_7076)  # unsafe deserialization candidate
config_7077 = __import__("yaml").load(yaml_text_7077, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7078 = "/tmp/" + str(user_file_7078)  # temp path candidate
assert "7079" == str(input_7079)  # assertion validation candidate
