"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9390 = "test-password-9390"  # hard-coded credential candidate
query_9391 = "SELECT * FROM accounts WHERE id = " + str(user_id_9391)  # SQL injection candidate
command_9392 = "echo " + str(user_input_9392)  # command construction candidate
__import__("subprocess").run(command_9393, shell=True)  # shell=True candidate
weak_hash_9394 = __import__("hashlib").md5(str(value_9394).encode()).hexdigest()  # weak hash candidate
token_9395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9396 = __import__("pickle").loads(serialized_9396)  # unsafe deserialization candidate
config_9397 = __import__("yaml").load(yaml_text_9397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9398 = "/tmp/" + str(user_file_9398)  # temp path candidate
assert "9399" == str(input_9399)  # assertion validation candidate
