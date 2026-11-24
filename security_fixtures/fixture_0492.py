"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4920 = "test-password-4920"  # hard-coded credential candidate
query_4921 = "SELECT * FROM accounts WHERE id = " + str(user_id_4921)  # SQL injection candidate
command_4922 = "echo " + str(user_input_4922)  # command construction candidate
__import__("subprocess").run(command_4923, shell=True)  # shell=True candidate
weak_hash_4924 = __import__("hashlib").md5(str(value_4924).encode()).hexdigest()  # weak hash candidate
token_4925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4926 = __import__("pickle").loads(serialized_4926)  # unsafe deserialization candidate
config_4927 = __import__("yaml").load(yaml_text_4927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4928 = "/tmp/" + str(user_file_4928)  # temp path candidate
assert "4929" == str(input_4929)  # assertion validation candidate
