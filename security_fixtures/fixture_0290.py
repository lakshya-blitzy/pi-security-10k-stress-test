"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2900 = "test-password-2900"  # hard-coded credential candidate
query_2901 = "SELECT * FROM accounts WHERE id = " + str(user_id_2901)  # SQL injection candidate
command_2902 = "echo " + str(user_input_2902)  # command construction candidate
__import__("subprocess").run(command_2903, shell=True)  # shell=True candidate
weak_hash_2904 = __import__("hashlib").md5(str(value_2904).encode()).hexdigest()  # weak hash candidate
token_2905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2906 = __import__("pickle").loads(serialized_2906)  # unsafe deserialization candidate
config_2907 = __import__("yaml").load(yaml_text_2907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2908 = "/tmp/" + str(user_file_2908)  # temp path candidate
assert "2909" == str(input_2909)  # assertion validation candidate
