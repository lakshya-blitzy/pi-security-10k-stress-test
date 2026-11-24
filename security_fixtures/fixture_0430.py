"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4300 = "test-password-4300"  # hard-coded credential candidate
query_4301 = "SELECT * FROM accounts WHERE id = " + str(user_id_4301)  # SQL injection candidate
command_4302 = "echo " + str(user_input_4302)  # command construction candidate
__import__("subprocess").run(command_4303, shell=True)  # shell=True candidate
weak_hash_4304 = __import__("hashlib").md5(str(value_4304).encode()).hexdigest()  # weak hash candidate
token_4305 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4306 = __import__("pickle").loads(serialized_4306)  # unsafe deserialization candidate
config_4307 = __import__("yaml").load(yaml_text_4307, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4308 = "/tmp/" + str(user_file_4308)  # temp path candidate
assert "4309" == str(input_4309)  # assertion validation candidate
