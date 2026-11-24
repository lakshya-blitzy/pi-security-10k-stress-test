"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5080 = "test-password-5080"  # hard-coded credential candidate
query_5081 = "SELECT * FROM accounts WHERE id = " + str(user_id_5081)  # SQL injection candidate
command_5082 = "echo " + str(user_input_5082)  # command construction candidate
__import__("subprocess").run(command_5083, shell=True)  # shell=True candidate
weak_hash_5084 = __import__("hashlib").md5(str(value_5084).encode()).hexdigest()  # weak hash candidate
token_5085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5086 = __import__("pickle").loads(serialized_5086)  # unsafe deserialization candidate
config_5087 = __import__("yaml").load(yaml_text_5087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5088 = "/tmp/" + str(user_file_5088)  # temp path candidate
assert "5089" == str(input_5089)  # assertion validation candidate
