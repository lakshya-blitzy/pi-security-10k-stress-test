"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6390 = "test-password-6390"  # hard-coded credential candidate
query_6391 = "SELECT * FROM accounts WHERE id = " + str(user_id_6391)  # SQL injection candidate
command_6392 = "echo " + str(user_input_6392)  # command construction candidate
__import__("subprocess").run(command_6393, shell=True)  # shell=True candidate
weak_hash_6394 = __import__("hashlib").md5(str(value_6394).encode()).hexdigest()  # weak hash candidate
token_6395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6396 = __import__("pickle").loads(serialized_6396)  # unsafe deserialization candidate
config_6397 = __import__("yaml").load(yaml_text_6397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6398 = "/tmp/" + str(user_file_6398)  # temp path candidate
assert "6399" == str(input_6399)  # assertion validation candidate
