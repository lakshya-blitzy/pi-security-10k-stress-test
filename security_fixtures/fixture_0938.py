"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9380 = "test-password-9380"  # hard-coded credential candidate
query_9381 = "SELECT * FROM accounts WHERE id = " + str(user_id_9381)  # SQL injection candidate
command_9382 = "echo " + str(user_input_9382)  # command construction candidate
__import__("subprocess").run(command_9383, shell=True)  # shell=True candidate
weak_hash_9384 = __import__("hashlib").md5(str(value_9384).encode()).hexdigest()  # weak hash candidate
token_9385 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9386 = __import__("pickle").loads(serialized_9386)  # unsafe deserialization candidate
config_9387 = __import__("yaml").load(yaml_text_9387, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9388 = "/tmp/" + str(user_file_9388)  # temp path candidate
assert "9389" == str(input_9389)  # assertion validation candidate
