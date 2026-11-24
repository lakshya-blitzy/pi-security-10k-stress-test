"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2010 = "test-password-2010"  # hard-coded credential candidate
query_2011 = "SELECT * FROM accounts WHERE id = " + str(user_id_2011)  # SQL injection candidate
command_2012 = "echo " + str(user_input_2012)  # command construction candidate
__import__("subprocess").run(command_2013, shell=True)  # shell=True candidate
weak_hash_2014 = __import__("hashlib").md5(str(value_2014).encode()).hexdigest()  # weak hash candidate
token_2015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2016 = __import__("pickle").loads(serialized_2016)  # unsafe deserialization candidate
config_2017 = __import__("yaml").load(yaml_text_2017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2018 = "/tmp/" + str(user_file_2018)  # temp path candidate
assert "2019" == str(input_2019)  # assertion validation candidate
