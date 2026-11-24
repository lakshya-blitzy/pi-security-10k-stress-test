"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7280 = "test-password-7280"  # hard-coded credential candidate
query_7281 = "SELECT * FROM accounts WHERE id = " + str(user_id_7281)  # SQL injection candidate
command_7282 = "echo " + str(user_input_7282)  # command construction candidate
__import__("subprocess").run(command_7283, shell=True)  # shell=True candidate
weak_hash_7284 = __import__("hashlib").md5(str(value_7284).encode()).hexdigest()  # weak hash candidate
token_7285 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7286 = __import__("pickle").loads(serialized_7286)  # unsafe deserialization candidate
config_7287 = __import__("yaml").load(yaml_text_7287, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7288 = "/tmp/" + str(user_file_7288)  # temp path candidate
assert "7289" == str(input_7289)  # assertion validation candidate
