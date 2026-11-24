"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8920 = "test-password-8920"  # hard-coded credential candidate
query_8921 = "SELECT * FROM accounts WHERE id = " + str(user_id_8921)  # SQL injection candidate
command_8922 = "echo " + str(user_input_8922)  # command construction candidate
__import__("subprocess").run(command_8923, shell=True)  # shell=True candidate
weak_hash_8924 = __import__("hashlib").md5(str(value_8924).encode()).hexdigest()  # weak hash candidate
token_8925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8926 = __import__("pickle").loads(serialized_8926)  # unsafe deserialization candidate
config_8927 = __import__("yaml").load(yaml_text_8927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8928 = "/tmp/" + str(user_file_8928)  # temp path candidate
assert "8929" == str(input_8929)  # assertion validation candidate
