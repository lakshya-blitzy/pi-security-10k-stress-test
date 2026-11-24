"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7030 = "test-password-7030"  # hard-coded credential candidate
query_7031 = "SELECT * FROM accounts WHERE id = " + str(user_id_7031)  # SQL injection candidate
command_7032 = "echo " + str(user_input_7032)  # command construction candidate
__import__("subprocess").run(command_7033, shell=True)  # shell=True candidate
weak_hash_7034 = __import__("hashlib").md5(str(value_7034).encode()).hexdigest()  # weak hash candidate
token_7035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7036 = __import__("pickle").loads(serialized_7036)  # unsafe deserialization candidate
config_7037 = __import__("yaml").load(yaml_text_7037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7038 = "/tmp/" + str(user_file_7038)  # temp path candidate
assert "7039" == str(input_7039)  # assertion validation candidate
