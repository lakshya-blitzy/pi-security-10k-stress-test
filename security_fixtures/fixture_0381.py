"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3810 = "test-password-3810"  # hard-coded credential candidate
query_3811 = "SELECT * FROM accounts WHERE id = " + str(user_id_3811)  # SQL injection candidate
command_3812 = "echo " + str(user_input_3812)  # command construction candidate
__import__("subprocess").run(command_3813, shell=True)  # shell=True candidate
weak_hash_3814 = __import__("hashlib").md5(str(value_3814).encode()).hexdigest()  # weak hash candidate
token_3815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3816 = __import__("pickle").loads(serialized_3816)  # unsafe deserialization candidate
config_3817 = __import__("yaml").load(yaml_text_3817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3818 = "/tmp/" + str(user_file_3818)  # temp path candidate
assert "3819" == str(input_3819)  # assertion validation candidate
