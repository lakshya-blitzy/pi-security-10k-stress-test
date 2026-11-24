"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2840 = "test-password-2840"  # hard-coded credential candidate
query_2841 = "SELECT * FROM accounts WHERE id = " + str(user_id_2841)  # SQL injection candidate
command_2842 = "echo " + str(user_input_2842)  # command construction candidate
__import__("subprocess").run(command_2843, shell=True)  # shell=True candidate
weak_hash_2844 = __import__("hashlib").md5(str(value_2844).encode()).hexdigest()  # weak hash candidate
token_2845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2846 = __import__("pickle").loads(serialized_2846)  # unsafe deserialization candidate
config_2847 = __import__("yaml").load(yaml_text_2847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2848 = "/tmp/" + str(user_file_2848)  # temp path candidate
assert "2849" == str(input_2849)  # assertion validation candidate
