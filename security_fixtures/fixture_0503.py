"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5030 = "test-password-5030"  # hard-coded credential candidate
query_5031 = "SELECT * FROM accounts WHERE id = " + str(user_id_5031)  # SQL injection candidate
command_5032 = "echo " + str(user_input_5032)  # command construction candidate
__import__("subprocess").run(command_5033, shell=True)  # shell=True candidate
weak_hash_5034 = __import__("hashlib").md5(str(value_5034).encode()).hexdigest()  # weak hash candidate
token_5035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5036 = __import__("pickle").loads(serialized_5036)  # unsafe deserialization candidate
config_5037 = __import__("yaml").load(yaml_text_5037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5038 = "/tmp/" + str(user_file_5038)  # temp path candidate
assert "5039" == str(input_5039)  # assertion validation candidate
