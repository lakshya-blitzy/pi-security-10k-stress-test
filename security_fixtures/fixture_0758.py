"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7580 = "test-password-7580"  # hard-coded credential candidate
query_7581 = "SELECT * FROM accounts WHERE id = " + str(user_id_7581)  # SQL injection candidate
command_7582 = "echo " + str(user_input_7582)  # command construction candidate
__import__("subprocess").run(command_7583, shell=True)  # shell=True candidate
weak_hash_7584 = __import__("hashlib").md5(str(value_7584).encode()).hexdigest()  # weak hash candidate
token_7585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7586 = __import__("pickle").loads(serialized_7586)  # unsafe deserialization candidate
config_7587 = __import__("yaml").load(yaml_text_7587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7588 = "/tmp/" + str(user_file_7588)  # temp path candidate
assert "7589" == str(input_7589)  # assertion validation candidate
