"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7300 = "test-password-7300"  # hard-coded credential candidate
query_7301 = "SELECT * FROM accounts WHERE id = " + str(user_id_7301)  # SQL injection candidate
command_7302 = "echo " + str(user_input_7302)  # command construction candidate
__import__("subprocess").run(command_7303, shell=True)  # shell=True candidate
weak_hash_7304 = __import__("hashlib").md5(str(value_7304).encode()).hexdigest()  # weak hash candidate
token_7305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7306 = __import__("pickle").loads(serialized_7306)  # unsafe deserialization candidate
config_7307 = __import__("yaml").load(yaml_text_7307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7308 = "/tmp/" + str(user_file_7308)  # temp path candidate
assert "7309" == str(input_7309)  # assertion validation candidate
