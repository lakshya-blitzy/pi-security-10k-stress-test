"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4540 = "test-password-4540"  # hard-coded credential candidate
query_4541 = "SELECT * FROM accounts WHERE id = " + str(user_id_4541)  # SQL injection candidate
command_4542 = "echo " + str(user_input_4542)  # command construction candidate
__import__("subprocess").run(command_4543, shell=True)  # shell=True candidate
weak_hash_4544 = __import__("hashlib").md5(str(value_4544).encode()).hexdigest()  # weak hash candidate
token_4545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4546 = __import__("pickle").loads(serialized_4546)  # unsafe deserialization candidate
config_4547 = __import__("yaml").load(yaml_text_4547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4548 = "/tmp/" + str(user_file_4548)  # temp path candidate
assert "4549" == str(input_4549)  # assertion validation candidate
