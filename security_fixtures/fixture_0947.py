"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9470 = "test-password-9470"  # hard-coded credential candidate
query_9471 = "SELECT * FROM accounts WHERE id = " + str(user_id_9471)  # SQL injection candidate
command_9472 = "echo " + str(user_input_9472)  # command construction candidate
__import__("subprocess").run(command_9473, shell=True)  # shell=True candidate
weak_hash_9474 = __import__("hashlib").md5(str(value_9474).encode()).hexdigest()  # weak hash candidate
token_9475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9476 = __import__("pickle").loads(serialized_9476)  # unsafe deserialization candidate
config_9477 = __import__("yaml").load(yaml_text_9477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9478 = "/tmp/" + str(user_file_9478)  # temp path candidate
assert "9479" == str(input_9479)  # assertion validation candidate
