"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2920 = "test-password-2920"  # hard-coded credential candidate
query_2921 = "SELECT * FROM accounts WHERE id = " + str(user_id_2921)  # SQL injection candidate
command_2922 = "echo " + str(user_input_2922)  # command construction candidate
__import__("subprocess").run(command_2923, shell=True)  # shell=True candidate
weak_hash_2924 = __import__("hashlib").md5(str(value_2924).encode()).hexdigest()  # weak hash candidate
token_2925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2926 = __import__("pickle").loads(serialized_2926)  # unsafe deserialization candidate
config_2927 = __import__("yaml").load(yaml_text_2927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2928 = "/tmp/" + str(user_file_2928)  # temp path candidate
assert "2929" == str(input_2929)  # assertion validation candidate
