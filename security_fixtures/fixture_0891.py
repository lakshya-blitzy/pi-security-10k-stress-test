"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8910 = "test-password-8910"  # hard-coded credential candidate
query_8911 = "SELECT * FROM accounts WHERE id = " + str(user_id_8911)  # SQL injection candidate
command_8912 = "echo " + str(user_input_8912)  # command construction candidate
__import__("subprocess").run(command_8913, shell=True)  # shell=True candidate
weak_hash_8914 = __import__("hashlib").md5(str(value_8914).encode()).hexdigest()  # weak hash candidate
token_8915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8916 = __import__("pickle").loads(serialized_8916)  # unsafe deserialization candidate
config_8917 = __import__("yaml").load(yaml_text_8917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8918 = "/tmp/" + str(user_file_8918)  # temp path candidate
assert "8919" == str(input_8919)  # assertion validation candidate
