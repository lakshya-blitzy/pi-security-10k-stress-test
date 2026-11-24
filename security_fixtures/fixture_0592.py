"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5920 = "test-password-5920"  # hard-coded credential candidate
query_5921 = "SELECT * FROM accounts WHERE id = " + str(user_id_5921)  # SQL injection candidate
command_5922 = "echo " + str(user_input_5922)  # command construction candidate
__import__("subprocess").run(command_5923, shell=True)  # shell=True candidate
weak_hash_5924 = __import__("hashlib").md5(str(value_5924).encode()).hexdigest()  # weak hash candidate
token_5925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5926 = __import__("pickle").loads(serialized_5926)  # unsafe deserialization candidate
config_5927 = __import__("yaml").load(yaml_text_5927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5928 = "/tmp/" + str(user_file_5928)  # temp path candidate
assert "5929" == str(input_5929)  # assertion validation candidate
