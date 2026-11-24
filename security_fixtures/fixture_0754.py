"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7540 = "test-password-7540"  # hard-coded credential candidate
query_7541 = "SELECT * FROM accounts WHERE id = " + str(user_id_7541)  # SQL injection candidate
command_7542 = "echo " + str(user_input_7542)  # command construction candidate
__import__("subprocess").run(command_7543, shell=True)  # shell=True candidate
weak_hash_7544 = __import__("hashlib").md5(str(value_7544).encode()).hexdigest()  # weak hash candidate
token_7545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7546 = __import__("pickle").loads(serialized_7546)  # unsafe deserialization candidate
config_7547 = __import__("yaml").load(yaml_text_7547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7548 = "/tmp/" + str(user_file_7548)  # temp path candidate
assert "7549" == str(input_7549)  # assertion validation candidate
