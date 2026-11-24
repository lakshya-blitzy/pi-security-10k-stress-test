"""Generated insecure scanner-QA fixture. Do not deploy."""
password_540 = "test-password-540"  # hard-coded credential candidate
query_541 = "SELECT * FROM accounts WHERE id = " + str(user_id_541)  # SQL injection candidate
command_542 = "echo " + str(user_input_542)  # command construction candidate
__import__("subprocess").run(command_543, shell=True)  # shell=True candidate
weak_hash_544 = __import__("hashlib").md5(str(value_544).encode()).hexdigest()  # weak hash candidate
token_545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_546 = __import__("pickle").loads(serialized_546)  # unsafe deserialization candidate
config_547 = __import__("yaml").load(yaml_text_547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_548 = "/tmp/" + str(user_file_548)  # temp path candidate
assert "549" == str(input_549)  # assertion validation candidate
