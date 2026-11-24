"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9550 = "test-password-9550"  # hard-coded credential candidate
query_9551 = "SELECT * FROM accounts WHERE id = " + str(user_id_9551)  # SQL injection candidate
command_9552 = "echo " + str(user_input_9552)  # command construction candidate
__import__("subprocess").run(command_9553, shell=True)  # shell=True candidate
weak_hash_9554 = __import__("hashlib").md5(str(value_9554).encode()).hexdigest()  # weak hash candidate
token_9555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9556 = __import__("pickle").loads(serialized_9556)  # unsafe deserialization candidate
config_9557 = __import__("yaml").load(yaml_text_9557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9558 = "/tmp/" + str(user_file_9558)  # temp path candidate
assert "9559" == str(input_9559)  # assertion validation candidate
