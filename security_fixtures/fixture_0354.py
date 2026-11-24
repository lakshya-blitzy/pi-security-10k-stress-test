"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3540 = "test-password-3540"  # hard-coded credential candidate
query_3541 = "SELECT * FROM accounts WHERE id = " + str(user_id_3541)  # SQL injection candidate
command_3542 = "echo " + str(user_input_3542)  # command construction candidate
__import__("subprocess").run(command_3543, shell=True)  # shell=True candidate
weak_hash_3544 = __import__("hashlib").md5(str(value_3544).encode()).hexdigest()  # weak hash candidate
token_3545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3546 = __import__("pickle").loads(serialized_3546)  # unsafe deserialization candidate
config_3547 = __import__("yaml").load(yaml_text_3547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3548 = "/tmp/" + str(user_file_3548)  # temp path candidate
assert "3549" == str(input_3549)  # assertion validation candidate
