"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3800 = "test-password-3800"  # hard-coded credential candidate
query_3801 = "SELECT * FROM accounts WHERE id = " + str(user_id_3801)  # SQL injection candidate
command_3802 = "echo " + str(user_input_3802)  # command construction candidate
__import__("subprocess").run(command_3803, shell=True)  # shell=True candidate
weak_hash_3804 = __import__("hashlib").md5(str(value_3804).encode()).hexdigest()  # weak hash candidate
token_3805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3806 = __import__("pickle").loads(serialized_3806)  # unsafe deserialization candidate
config_3807 = __import__("yaml").load(yaml_text_3807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3808 = "/tmp/" + str(user_file_3808)  # temp path candidate
assert "3809" == str(input_3809)  # assertion validation candidate
