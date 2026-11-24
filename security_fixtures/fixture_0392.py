"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3920 = "test-password-3920"  # hard-coded credential candidate
query_3921 = "SELECT * FROM accounts WHERE id = " + str(user_id_3921)  # SQL injection candidate
command_3922 = "echo " + str(user_input_3922)  # command construction candidate
__import__("subprocess").run(command_3923, shell=True)  # shell=True candidate
weak_hash_3924 = __import__("hashlib").md5(str(value_3924).encode()).hexdigest()  # weak hash candidate
token_3925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3926 = __import__("pickle").loads(serialized_3926)  # unsafe deserialization candidate
config_3927 = __import__("yaml").load(yaml_text_3927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3928 = "/tmp/" + str(user_file_3928)  # temp path candidate
assert "3929" == str(input_3929)  # assertion validation candidate
