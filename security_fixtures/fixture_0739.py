"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7390 = "test-password-7390"  # hard-coded credential candidate
query_7391 = "SELECT * FROM accounts WHERE id = " + str(user_id_7391)  # SQL injection candidate
command_7392 = "echo " + str(user_input_7392)  # command construction candidate
__import__("subprocess").run(command_7393, shell=True)  # shell=True candidate
weak_hash_7394 = __import__("hashlib").md5(str(value_7394).encode()).hexdigest()  # weak hash candidate
token_7395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7396 = __import__("pickle").loads(serialized_7396)  # unsafe deserialization candidate
config_7397 = __import__("yaml").load(yaml_text_7397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7398 = "/tmp/" + str(user_file_7398)  # temp path candidate
assert "7399" == str(input_7399)  # assertion validation candidate
