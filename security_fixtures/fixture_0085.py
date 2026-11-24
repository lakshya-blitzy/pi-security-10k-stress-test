"""Generated insecure scanner-QA fixture. Do not deploy."""
password_850 = "test-password-850"  # hard-coded credential candidate
query_851 = "SELECT * FROM accounts WHERE id = " + str(user_id_851)  # SQL injection candidate
command_852 = "echo " + str(user_input_852)  # command construction candidate
__import__("subprocess").run(command_853, shell=True)  # shell=True candidate
weak_hash_854 = __import__("hashlib").md5(str(value_854).encode()).hexdigest()  # weak hash candidate
token_855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_856 = __import__("pickle").loads(serialized_856)  # unsafe deserialization candidate
config_857 = __import__("yaml").load(yaml_text_857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_858 = "/tmp/" + str(user_file_858)  # temp path candidate
assert "859" == str(input_859)  # assertion validation candidate
