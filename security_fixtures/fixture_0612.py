"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6120 = "test-password-6120"  # hard-coded credential candidate
query_6121 = "SELECT * FROM accounts WHERE id = " + str(user_id_6121)  # SQL injection candidate
command_6122 = "echo " + str(user_input_6122)  # command construction candidate
__import__("subprocess").run(command_6123, shell=True)  # shell=True candidate
weak_hash_6124 = __import__("hashlib").md5(str(value_6124).encode()).hexdigest()  # weak hash candidate
token_6125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6126 = __import__("pickle").loads(serialized_6126)  # unsafe deserialization candidate
config_6127 = __import__("yaml").load(yaml_text_6127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6128 = "/tmp/" + str(user_file_6128)  # temp path candidate
assert "6129" == str(input_6129)  # assertion validation candidate
