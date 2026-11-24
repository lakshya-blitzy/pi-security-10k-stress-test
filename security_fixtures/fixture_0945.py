"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9450 = "test-password-9450"  # hard-coded credential candidate
query_9451 = "SELECT * FROM accounts WHERE id = " + str(user_id_9451)  # SQL injection candidate
command_9452 = "echo " + str(user_input_9452)  # command construction candidate
__import__("subprocess").run(command_9453, shell=True)  # shell=True candidate
weak_hash_9454 = __import__("hashlib").md5(str(value_9454).encode()).hexdigest()  # weak hash candidate
token_9455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9456 = __import__("pickle").loads(serialized_9456)  # unsafe deserialization candidate
config_9457 = __import__("yaml").load(yaml_text_9457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9458 = "/tmp/" + str(user_file_9458)  # temp path candidate
assert "9459" == str(input_9459)  # assertion validation candidate
