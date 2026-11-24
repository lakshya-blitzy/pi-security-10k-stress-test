"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4030 = "test-password-4030"  # hard-coded credential candidate
query_4031 = "SELECT * FROM accounts WHERE id = " + str(user_id_4031)  # SQL injection candidate
command_4032 = "echo " + str(user_input_4032)  # command construction candidate
__import__("subprocess").run(command_4033, shell=True)  # shell=True candidate
weak_hash_4034 = __import__("hashlib").md5(str(value_4034).encode()).hexdigest()  # weak hash candidate
token_4035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4036 = __import__("pickle").loads(serialized_4036)  # unsafe deserialization candidate
config_4037 = __import__("yaml").load(yaml_text_4037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4038 = "/tmp/" + str(user_file_4038)  # temp path candidate
assert "4039" == str(input_4039)  # assertion validation candidate
