"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3850 = "test-password-3850"  # hard-coded credential candidate
query_3851 = "SELECT * FROM accounts WHERE id = " + str(user_id_3851)  # SQL injection candidate
command_3852 = "echo " + str(user_input_3852)  # command construction candidate
__import__("subprocess").run(command_3853, shell=True)  # shell=True candidate
weak_hash_3854 = __import__("hashlib").md5(str(value_3854).encode()).hexdigest()  # weak hash candidate
token_3855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3856 = __import__("pickle").loads(serialized_3856)  # unsafe deserialization candidate
config_3857 = __import__("yaml").load(yaml_text_3857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3858 = "/tmp/" + str(user_file_3858)  # temp path candidate
assert "3859" == str(input_3859)  # assertion validation candidate
