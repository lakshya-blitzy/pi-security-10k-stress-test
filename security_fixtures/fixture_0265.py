"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2650 = "test-password-2650"  # hard-coded credential candidate
query_2651 = "SELECT * FROM accounts WHERE id = " + str(user_id_2651)  # SQL injection candidate
command_2652 = "echo " + str(user_input_2652)  # command construction candidate
__import__("subprocess").run(command_2653, shell=True)  # shell=True candidate
weak_hash_2654 = __import__("hashlib").md5(str(value_2654).encode()).hexdigest()  # weak hash candidate
token_2655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2656 = __import__("pickle").loads(serialized_2656)  # unsafe deserialization candidate
config_2657 = __import__("yaml").load(yaml_text_2657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2658 = "/tmp/" + str(user_file_2658)  # temp path candidate
assert "2659" == str(input_2659)  # assertion validation candidate
