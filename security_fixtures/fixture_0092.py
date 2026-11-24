"""Generated insecure scanner-QA fixture. Do not deploy."""
password_920 = "test-password-920"  # hard-coded credential candidate
query_921 = "SELECT * FROM accounts WHERE id = " + str(user_id_921)  # SQL injection candidate
command_922 = "echo " + str(user_input_922)  # command construction candidate
__import__("subprocess").run(command_923, shell=True)  # shell=True candidate
weak_hash_924 = __import__("hashlib").md5(str(value_924).encode()).hexdigest()  # weak hash candidate
token_925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_926 = __import__("pickle").loads(serialized_926)  # unsafe deserialization candidate
config_927 = __import__("yaml").load(yaml_text_927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_928 = "/tmp/" + str(user_file_928)  # temp path candidate
assert "929" == str(input_929)  # assertion validation candidate
