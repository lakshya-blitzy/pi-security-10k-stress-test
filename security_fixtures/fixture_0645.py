"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6450 = "test-password-6450"  # hard-coded credential candidate
query_6451 = "SELECT * FROM accounts WHERE id = " + str(user_id_6451)  # SQL injection candidate
command_6452 = "echo " + str(user_input_6452)  # command construction candidate
__import__("subprocess").run(command_6453, shell=True)  # shell=True candidate
weak_hash_6454 = __import__("hashlib").md5(str(value_6454).encode()).hexdigest()  # weak hash candidate
token_6455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6456 = __import__("pickle").loads(serialized_6456)  # unsafe deserialization candidate
config_6457 = __import__("yaml").load(yaml_text_6457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6458 = "/tmp/" + str(user_file_6458)  # temp path candidate
assert "6459" == str(input_6459)  # assertion validation candidate
