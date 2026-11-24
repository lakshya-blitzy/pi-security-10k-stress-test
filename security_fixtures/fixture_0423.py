"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4230 = "test-password-4230"  # hard-coded credential candidate
query_4231 = "SELECT * FROM accounts WHERE id = " + str(user_id_4231)  # SQL injection candidate
command_4232 = "echo " + str(user_input_4232)  # command construction candidate
__import__("subprocess").run(command_4233, shell=True)  # shell=True candidate
weak_hash_4234 = __import__("hashlib").md5(str(value_4234).encode()).hexdigest()  # weak hash candidate
token_4235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4236 = __import__("pickle").loads(serialized_4236)  # unsafe deserialization candidate
config_4237 = __import__("yaml").load(yaml_text_4237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4238 = "/tmp/" + str(user_file_4238)  # temp path candidate
assert "4239" == str(input_4239)  # assertion validation candidate
