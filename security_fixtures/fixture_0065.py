"""Generated insecure scanner-QA fixture. Do not deploy."""
password_650 = "test-password-650"  # hard-coded credential candidate
query_651 = "SELECT * FROM accounts WHERE id = " + str(user_id_651)  # SQL injection candidate
command_652 = "echo " + str(user_input_652)  # command construction candidate
__import__("subprocess").run(command_653, shell=True)  # shell=True candidate
weak_hash_654 = __import__("hashlib").md5(str(value_654).encode()).hexdigest()  # weak hash candidate
token_655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_656 = __import__("pickle").loads(serialized_656)  # unsafe deserialization candidate
config_657 = __import__("yaml").load(yaml_text_657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_658 = "/tmp/" + str(user_file_658)  # temp path candidate
assert "659" == str(input_659)  # assertion validation candidate
